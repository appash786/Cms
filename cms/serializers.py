from rest_framework import serializers
from .models import Project, KeyFeature, TechCategory, Technology, PageSEO, PageKeyword

# --- Project Serializers ---

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name']

class TechCategorySerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = TechCategory
        fields = ['id', 'name', 'technologies']

class KeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = ['id', 'feature_image_url', 'title']

class ProjectListSerializer(serializers.ModelSerializer):
    """Lighter serializer for portfolio list page"""
    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'subtitle_summary', 'hero_banner_url', 'project_Published_date']

class ProjectDetailSerializer(serializers.ModelSerializer):
    """Full serializer for dynamic project detail page & metadata"""
    key_features = KeyFeatureSerializer(many=True, read_only=True)
    tech_categories = TechCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'subtitle_summary', 'live_demo_url', 'github_url',
            'hero_banner_url', 'client_name', 'timeline', 'showcase_summary',
            'mockup_image_url', 'the_challenge', 'our_approach',
            'meta_title', 'meta_description', 'og_image',
            'key_features', 'tech_categories', 'project_Published_date'
        ]


# --- Page SEO Serializers ---

class PageKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageKeyword
        fields = ['keyword']

class PageSEOSerializer(serializers.ModelSerializer):
    keywords = serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='keyword'
    )
    knows_about = serializers.SerializerMethodField()
    same_as_links = serializers.SerializerMethodField()

    class Meta:
        model = PageSEO
        fields = [
            'page_name', 'slug', 'site_url', 'title', 'description', 
            'author_name', 'creator', 'canonical_url', 'keywords',
            'og_title', 'og_description', 'og_image_url', 'og_image_alt', 
            'locale', 'site_name', 'twitter_card',
            'favicon_url', 'icon_96_url', 'apple_icon_url',
            'index', 'follow',
            'job_title', 'address_region', 'address_country', 'knows_about', 'same_as_links'
        ]

    def get_knows_about(self, obj):
        if obj.knows_about:
            return [item.strip() for item in obj.knows_about.split(',') if item.strip()]
        return []

    def get_same_as_links(self, obj):
        if obj.same_as_links:
            return [line.strip() for line in obj.same_as_links.splitlines() if line.strip()]
        return []