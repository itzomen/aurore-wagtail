"""
Read more:
https://stackoverflow.com/questions/41956709/custom-representation-of-streamfield-in-rest-api
"""
import wagtail
from rest_framework import serializers


class WagtailImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wagtail.images.get_image_model()
        fields = ["title", "file", "width", "height", "file_size"]


class WagtailDocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wagtail.documents.get_document_model()
        fields = ["title", "file", "file_size"]
