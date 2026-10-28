import nested_admin
from django.contrib import admin
from .models import Project, KeyFeature, TechCategory, Technology,PageSEO, PageKeyword

class KeyFeatureInline(nested_admin.NestedTabularInline):
    model = KeyFeature
    extra = 3

class TechnologyInline(nested_admin.NestedTabularInline):
    model = Technology
    extra = 3  # Adds keyword tag rows

class TechCategoryInline(nested_admin.NestedTabularInline):
    model = TechCategory
    inlines = [TechnologyInline]
    extra = 2



class PageKeywordInline(nested_admin.NestedTabularInline):
    model = PageKeyword
    extra = 5  # Provides empty inline rows for adding keywords



@admin.register(Project)
class ProjectAdmin(nested_admin.NestedModelAdmin):
    inlines = [KeyFeatureInline, TechCategoryInline]
    list_display = ('title', 'slug', 'project_Published_date', 'is_published')
    
    # Organize fields with a dedicated SEO section
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'subtitle_summary', 'client_name', 'timeline', 'is_published', 'project_Published_date')
        }),
        ('Links & Media', {
            'fields': ('hero_banner_url', 'mockup_image_url', 'live_demo_url', 'github_url')
        }),
        ('Content Sections', {
            'fields': ('showcase_summary', 'the_challenge', 'our_approach')
        }),
        ('SEO & Metadata Management', {
            'classes': ('collapse',),  # Makes this section collapsible in the admin
            'fields': ('slug', 'meta_title', 'meta_description', 'og_image'),
        }),
    )

@admin.register(PageSEO)
class PageSEOAdmin(nested_admin.NestedModelAdmin):
    inlines = [PageKeywordInline]
    list_display = ('page_name', 'slug', 'title', 'index', 'follow')

    fieldsets = (
        ('Page Identification', {
            'fields': ('page_name', 'slug', 'site_url')
        }),
        ('Core Metadata', {
            'fields': ('title', 'description', 'author_name', 'creator', 'canonical_url')
        }),
        ('Open Graph & Twitter', {
            'classes': ('collapse',),
            'fields': (
                'og_title', 'og_description', 'og_image_url', 
                'og_image_alt', 'locale', 'site_name', 'twitter_card'
            )
        }),
        ('Icons & Favicon', {
            'classes': ('collapse',),
            'fields': ('favicon_url', 'icon_96_url', 'apple_icon_url')
        }),
        ('Robots & Indexing', {
            'classes': ('collapse',),
            'fields': ('index', 'follow')
        }),
        ('JSON-LD / Schema.org', {
            'classes': ('collapse',),
            'fields': ('job_title', 'address_region', 'address_country', 'knows_about', 'same_as_links')
        }),
    )