
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, ForumPost, Donation, ProductListing, Service, Category
from .forms import ListingForm, ServiceForm, ForumPostForm, CommentForm, DonationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from django.http import JsonResponse
from .mpesa import Mpesa
from django.contrib import messages

#Donation

def donation_form(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            donor_name = form.cleaned_data['donor_name']
            donor_phone_number = form.cleaned_data['donor_phone_number']
            amount = form.cleaned_data['amount']

            # Initiate M-Pesa STK push
            try:
                response = Mpesa.stk_push(donor_phone_number, amount)
                if response.get('ResponseCode') == '0':  # Successful transaction
                    # Save the donation to the database
                    donation = Donation(
                        donor_name=donor_name,
                        donor_phone_number=donor_phone_number,
                        amount=amount,
                        payment_method="M-Pesa"
                    )
                    donation.save()

                    # Show success message
                    messages.success(request, "Payment request sent. Please check your phone to complete the transaction.")
                    return redirect('donation_success', donation_id=donation.id)  # Redirect to the success page
                else:
                    # Handle failed payment
                    messages.error(request, f"Payment failed: {response.get('errorMessage', 'Unknown error')}")
                    return render(request, 'donation_form.html', {'form': form})  # Stay on the form page

            except Exception as e:
                # Handle any exception that occurs during the STK push
                messages.error(request, "There was an issue processing your donation. Please try again later.")
                return render(request, 'donation_form.html', {'form': form})  # Stay on the form page

    else:
        form = DonationForm()

    return render(request, 'donation_form.html', {'form': form})

def current_donations(request):
    donations = Donation.objects.all().order_by('-created_at')  # Ordering by creation date
    return render(request, 'current_donations.html', {'donations': donations})

def mpesa_callback(request):
    if request.method == 'POST':
        # Log or process the M-Pesa callback response
        print(request.body)  # For debugging, print the request body
        return JsonResponse({'ResultCode': 0, 'ResultDesc': 'Accepted'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


#Home
def home(request):
    listings = Listing.objects.all()
    services = Service.objects.all()
    return render(request, 'home.html', {'listings': listings, 'services': services})



# Item Listing
def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the listing to the database
            return redirect('listing_success')  # Redirect to a success page or listing page
    else:
        form = ListingForm()

    categories = Category.objects.all()  # Get all categories
    return render(request, 'add_listing.html', {'form': form, 'categories': categories})




def listing_success(request, listing_id):
    # Get the listing object based on the listing_id
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listing_success.html', {'listing': listing})

def current_listings(request):
    # Fetch all listings from the database
    listings = Listing.objects.all()
    # Render the current_listings.html template with the listings context
    return render(request, 'current_listings.html', {'listings': listings})
def listing_detail(request, id):
    # Fetch the listing with the given ID
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'listing_detail.html', {'listing': listing})

#Forum

def forum_list(request):
    # Get all forum posts (formerly discussions)
    posts = ForumPost.objects.all()
    return render(request, 'forum.html', {'posts': posts})

def forum_detail(request, id):
    post = get_object_or_404(ForumPost, id=id)
    return render(request, 'forum_detail.html', {'post': post})

def forum(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new post
            return redirect('forum')  # Redirect to the forum page after posting
    else:
        form = ForumPostForm()

    posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'forum.html', {'posts': posts, 'form': form})

def forum_detail(request, id):
    post = get_object_or_404(ForumPost, id=id)
    comments = post.comments.all()  # Get all comments for the post

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post  # Link the comment to the post
            comment.save()
            return redirect('forum_detail', id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'forum_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })


def ongoing_discussions(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)  # Fetch post by pk
    comments = post.comments.all()  # Fetch all comments related to the post
    comment_form = CommentForm()  # Initialize the comment form

    if request.method == "POST" and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post  # Link comment to the specific forum post
        comment.save()

    return render(request, 'ongoing_discussions.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })





# View for Add Service
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})


def view_services(request):
    # Fetch all categories and product listings
    categories = Category.objects.all()  # Fetch all categories
    services = Service.objects.all() # Fetch all product listings

    # Pass the data to the template
    return render(request, 'view_services.html', {
        'categories': categories,
        'services': services
    })


def ongoing_discussions(request):
    discussions = ForumPost.objects.all() # Get all forum posts
    return render(request, 'ongoing_discussions.html', {'discussions': discussions})




#Registration

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})





# About Us view
def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')


