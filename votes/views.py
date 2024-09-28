from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review


def product_list(request):
    products = Product.objects.all()
    
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        rating = request.POST.get('rating')

        if author and text and rating:
            Review.objects.create(
                product=product,
                author=author,
                text=text,
                rating=int(rating)
            )
            return redirect('product_detail', pk=product.pk)
        
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})