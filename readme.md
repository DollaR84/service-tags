#service-tags
<h1>Service Tags</h1>
This services for search users by tags
<br><hr><br>
<h2>Service tags API:</h2>
<h4>For not authenticated users:</h4>
<ul>
<li>tags/ - show list all tags;</li>
</ul>

<h4>For authenticated users:</h4>
<ul>
  <li>for admin:<ul>
    <li>tags/<str:tags> - show users list all with have tags;</li>
    <li>users_list/ - show users all information;</li>
    </ul></li>

  <li>user:<ul>
  <li>user_tag/ - show user information and tags by authenticated;</li>
    <li>user_tag/<int:pk> - show user information and tags by id;</li>
    </ul></li></ul>

<br><hr><br>
<h2>Installations:</h2>
Before running service need run next steps:
<ul>
<li>docker-compose run tags python manage.py migrate</li>
<li>docker-compose run tags manage.py createsuperuser</li>
</ul>
