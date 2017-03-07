from rest_framework.serializers import  ModelSerializer, HyperlinkedIdentityField, SerializerMethodField


from posts.models import Post


post_url = HyperlinkedIdentityField(
	view_name='posts-api:detail', 
	lookup_field='slug'
	)

delete_urls = HyperlinkedIdentityField(
	view_name='posts-api:delete', 
	lookup_field='slug'
	)

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			"title" ,
			"content" ,
			# "id" ,
			"publish",
			# "slug",	
		]


class PostDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	image = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			"title" ,
			"content" ,
			"id" ,
			"publish",
			"slug",
			"user",
			"image",
		]
	def get_user(self, obj):
		return str(obj.user.username)

	def get_image(self, obj):
		try:
			image = obj.image.path
		except:
			image = None
		return image



class PostListSerializer(ModelSerializer):
	url = post_url
	user = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			"url",
			"title",
			"content" ,
			"id" ,
			"publish",
			'user',
		]
	def get_user(self, obj):
		return str(obj.user.username)


# new_item = {
	
# 			"title" :"New API Post" ,
# 			"content": "Post created using API",
# 			"publish": "2017-2-12",
# 			"slug": "new-slug-from-shell",
# }

# new_data = PostDetailSerializer(obj, data=new_item)
# if new_data.is_valid():
# 	new_data.save()
# else:
# 	print(new_data.errors)