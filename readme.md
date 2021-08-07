#service-tags
This services for search users by tags

Service tags API:
all API work for authenticated users.

  for admin:
    tags/ - show list all tags;
    tags/<str:tags> - show users list all with have tags;
    users_list/ - show users all information;

  user:
  user_tag/ - show user information and tags by authenticated;
    user_tag/<int:pk> - show user information and tags by id;
