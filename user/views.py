from django.shortcuts import render
from django.contrib.auth.models import User

from user.models import UserInformation, GalleryImage


def user_profile(request):
    # first_admin_user_info = UserInformation.objects.filter(user__is_staff=True).order_by('user__id').first()
    all_professional_names = UserInformation.objects.values_list('professional_names__name', flat=True).distinct()
    all_services = UserInformation.objects.values('services__name', 'services__description').distinct()
    user_info = UserInformation.objects.first()
    gallery_images = GalleryImage.objects.all()
    user_information = UserInformation.objects.get(user=request.user)

    print('++++++++++++++++++++++++++')
    print(user_information)
    # print(len(user_information))

    # Pass the message to the template using the context dictionary
    context = {'name': user_information.name,
               'all_professional_names': all_professional_names,
               'all_services': all_services,
               'user_description': user_info.personal_information.description,
               'user_phone': user_info.personal_information.phone,
               'user_email': user_info.personal_information.email,
               'user_twitter': user_info.personal_information.twitter,
               'user_skills': user_info.skills.values('name').distinct(),
               'gallery_images': gallery_images,
               'total_clients': user_information.total_clients,
               'total_projects': user_information.total_projects,
               'total_awards': user_information.total_awards,
               'total_years_experience': user_information.total_years_experience,
               'address': user_information.address,
               }

    return render(request, 'index04b9.html', context)
