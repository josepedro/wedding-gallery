from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import Photo

import logging

LOGGER = logging.getLogger(__name__)

def like_photo(request):
    photo_id = request.GET.get('photo_id')

    try:
        photo = Photo.objects.get(id = photo_id)
        photo.likes += 1
        photo.save()

        LOGGER.info('Photo like was update with success.')
        return JsonResponse(status=200, data={'status': True, 'number_likes': photo.likes})

    except Photo.DoesNotExist as exception:
        LOGGER.exception('Failed due %s', exception)
        return JsonResponse(status=404)

def change_status_photo(request):
    photo_id = request.GET.get('photo_id')
    photo_status = request.GET.get('photo_status')

    try:
        photo = Photo.objects.get(id = photo_id)
        photo.status = photo_status
        photo.save()

        LOGGER.info('Photo was update with success.')
        return JsonResponse(status=200, data={'status': True})

    except Photo.DoesNotExist as exception:
        LOGGER.exception('Failed due %s', exception)
        return JsonResponse(status=404)

class PhotoCreateView(CreateView):
    model = Photo
    fields = ['upload', ]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(PhotoCreateView, self).get_context_data(**kwargs)
        photos = Photo.objects.all()
        context['photos'] = photos
        return context

class PhotoSortedByLikesView(TemplateView):
    template_name = "core/photo_form.html"

    def get_context_data(self, **kwargs):
        context = super(PhotoSortedByLikesView, self).get_context_data(**kwargs)
        photos = Photo.objects.all()
        context['photos'] = sorted(photos, key=lambda t: t.likes, reverse=True)
        return context

class PhotoSortedByUploadView(TemplateView):
    template_name = "core/photo_form.html"

    def get_context_data(self, **kwargs):
        context = super(PhotoSortedByUploadView, self).get_context_data(**kwargs)
        photos = Photo.objects.all()
        context['photos'] = sorted(photos, key=lambda t: t.uploaded_at, reverse=True)
        return context

    
