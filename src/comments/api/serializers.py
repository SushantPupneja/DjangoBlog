from rest_framework.serializers import ModelSerializer

from comments.models import Comment

class CommentListAPISerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = [
			'id',
    		'content_type', 
    		'object_id', 
    		'parent' ,    
    		'content',
		]
	