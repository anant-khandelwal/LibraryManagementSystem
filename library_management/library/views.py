from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from .models import Book, Member,Lended
from .forms import BookForm, MemberForm,LendForm,ReturnForm
import datetime
from django.db.models import Q


def dashboard(request):
    members_with_debt = Member.objects.filter(debt__gte=500)

    return render(request,'dashboard.html',{'mwd':members_with_debt})

def books_view(request):
    books = Book.objects.all()
    return render(request, "books.html",{'books':books})

def members_view(request):
    members = Member.objects.all()
    return render(request,"members.html",{'members':members})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'addBook.html', {'form': form})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm()
    return render(request, 'addMember.html', {'form': form})



def lend_book(request):
    if request.method == 'POST':
        form = LendForm(request.POST)
        if form.is_valid():
            lending_instance = form.save()
            lending_instance.book.qty-=1
            lending_instance.book.save()
            return redirect('lendings')
    else:
        form = LendForm()
    return render(request, 'lend_book.html', {'form': form})

def lendings(request):
    lendings = Lended.objects.all()
    return render(request, 'lendings.html', {'lendings': lendings})



def return_book(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            lending_id = request.POST.get('lending')
            lending = Lended.objects.get(pk=lending_id)
            lending.returned = True
            lending.save()
            lending.member.debt += (datetime.date.today() - lending.issue_date).days * lending.book.per_day_charge
            lending.member.save()
            lending.book.qty+=1
            lending.book.save()
            return redirect('lendings')
    else:
        form = ReturnForm()
    return render(request, 'return_book.html', {'form': form, 'lendings': Lended.objects.filter(returned=False)})


def search_books(request):
    if request.method == 'GET':
        val = request.GET.get('name')  
        books = Book.objects.filter(Q(title__icontains=val) | Q(author__icontains=val))   
        return render(request, 'search_results.html', {'books': books})
    return render(request, 'search_books.html')


def debt_view(request):
    member = Member.objects.filter(debt__gt=0)
    return render(request, 'debts.html',{'members':member})


def settle_debt(request,member_id):
    member = Member.objects.get(id=member_id)
    if request.method=='POST':
        val =int(request.POST.get('amt'))
        if val>member.debt:
            return render(request,'settle_debt.html',{'member':member,"error":"The amount is greater than debt"})
        member.debt-=val
        member.save()
        return redirect(reverse('settle_debt',kwargs={'member_id':member_id}))
    return render(request,'settle_debt.html',{'member':member})



import requests
from django.shortcuts import render, redirect, reverse
from .models import Book

def import_books(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        api_url = "https://frappe.io/api/method/frappe-library"

        if title:
            data = {
                "title": title
            }
        elif author:
            data = {
                'authors': author
            }
        else:
            return render(request, 'import_books.html', {'error': "Please enter a valid name"})
        
        response = requests.post(api_url, data=data)
        book_data = response.json()

        if not book_data or not book_data.get('message'):
            return render(request, 'import_books.html', {'error': "No such book found in the records"})
        
        book_data = book_data['message'][0]

        # Check if the book already exists in the database
        existing_book = Book.objects.filter(title=book_data["title"], author=book_data["authors"]).first()

        # Check if the retrieved book data matches the provided author or title exactly
        if (title and book_data.get("title") == title) or (author and book_data.get("authors") == author):
            if existing_book:
                # If the book exists, update the quantity
                existing_book.qty += 1
                existing_book.save()
            else:
                # If the book doesn't exist, create a new entry
                Book.objects.create(
                    title=book_data["title"],
                    author=book_data["authors"],
                    isbn=book_data.get("isbn", ""),
                    isbn13=book_data.get("isbn13", ""),
                    publisher=book_data.get("publisher", ""),
                    num_pages=book_data.get("num_pages", 0),
                    per_day_charge=0.5,  # Adjust the per day charge as needed
                    qty=1,
                )
        
        return redirect(reverse('books'))
    
    return render(request, 'import_books.html')
