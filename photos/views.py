from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Photo
# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html',context)

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html',{'photo':photo})



def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data  = request.POST
        image = request.FILES.get('image')

        # 1️⃣ Pick (or create) exactly ONE Category object
        if data.get('category') and data['category'] != 'none':
            selected_category = get_object_or_404(Category, id=data['category'])
        elif data.get('category_new'):
            selected_category, _ = Category.objects.get_or_create(
                name=data['category_new'].strip()
            )
        else:
            selected_category = None    # optional category

        # 2️⃣ Create the photo with that single Category instance
        Photo.objects.create(
            category    = selected_category,
            description = data['description'],
            image       = image,
        )

        return redirect('gallery')

    # GET request → show the form
    return render(request, 'photos/add.html', {'categories': categories})
