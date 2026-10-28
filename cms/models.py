from django.db import models
from django.utils.text import slugify
class Project(models.Model):
    # 1. Header & Overview
    title = models.CharField(max_length=100)                  # e.g., "ECOMMERCE APPLICATION"
    subtitle_summary = models.TextField(max_length=200)      # Summary below the title[cite: 7]
    live_demo_url = models.URLField(blank=True, null=True)   # "Live" link[cite: 7]
    github_url = models.URLField(blank=True, null=True)      # "GitHub" link[cite: 7]

    # 2. Hero Banner
    hero_banner_url = models.URLField()                      # Large top banner image[cite: 7]

    # 3. Meta Info (Client & Timeline)
    client_name = models.CharField(max_length=50, blank=True, null=True)   # e.g., "Innovations Pvt Ltd"[cite: 7]
    timeline = models.CharField(max_length=30, blank=True, null=True)      # e.g., "2-3 weeks"[cite: 7]

    # 4. Showcase Section
    showcase_summary = models.TextField(max_length=300)      # Descriptive text[cite: 7]
    mockup_image_url = models.URLField()                     # Frame image below showcase text[cite: 7]

    # 5. Core Sections
    the_challenge = models.TextField()                       # Challenge details[cite: 7]
    our_approach = models.TextField()                        # Approach details[cite: 7]

    # System fields
    project_Published_date = models.DateTimeField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    # === NEW: SEO & Metadata Fields ===
    slug = models.SlugField(unique=True, max_length=120, blank=True, help_text="URL-friendly version of the title (auto-generated if empty)")
    meta_title = models.CharField(max_length=60, blank=True, null=True, help_text="SEO title for search engines (recommended: max 60 chars)")
    meta_description = models.CharField(max_length=160, blank=True, null=True, help_text="SEO description snippet (recommended: max 160 chars)")
    og_image = models.URLField(blank=True, null=True, help_text="Thumbnail image for social media shares (Twitter, LinkedIn, etc.)")

    # Auto-generate slug from title if left blank
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



# 6. Key Features (For the 3 feature cards)
class KeyFeature(models.Model):
    project = models.ForeignKey(Project, related_name='key_features', on_delete=models.CASCADE)
    image_url = models.URLField()                            # Feature image[cite: 7]
    title = models.CharField(max_length=100)                 # Feature title

    def __str__(self):
        return f"{self.project.title} - {self.title}"


class TechCategory(models.Model):
    project = models.ForeignKey(Project, related_name='tech_categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # e.g., "Web development", "Design"

    def __str__(self):
        return f"{self.project.title} - {self.name}"

class Technology(models.Model):
    category = models.ForeignKey(TechCategory, related_name='technologies', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # e.g., "GSAP", "Next.js", "Figma"

    def __str__(self):
        return self.name



    








class PageSEO(models.Model):
    page_name = models.CharField(
        max_length=100, 
        unique=True, 
        help_text="Name of the page (e.g., Home, About, Projects)"
    )
    slug = models.SlugField(
        unique=True, 
        max_length=120, 
        help_text="URL route identifier (e.g., 'home', 'about')"
    )

    # Basic Metadata
    site_url = models.URLField(default="https://appzvile.com")
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=300)
    author_name = models.CharField(max_length=100, default="Appash A S")
    creator = models.CharField(max_length=100, default="Appash A S")
    canonical_url = models.CharField(max_length=200, default="/")

    # OpenGraph & Twitter
    og_title = models.CharField(max_length=120, blank=True, null=True)
    og_description = models.TextField(max_length=300, blank=True, null=True)
    og_image_url = models.URLField(blank=True, null=True, help_text="1200x630 image URL for OG & Twitter")
    og_image_alt = models.CharField(max_length=200, blank=True, null=True)
    locale = models.CharField(max_length=10, default="en_IN")
    site_name = models.CharField(max_length=100, default="Appash A S")
    twitter_card = models.CharField(max_length=50, default="summary_large_image")

    # Icons & Favicons
    favicon_url = models.URLField(blank=True, null=True)
    icon_96_url = models.URLField(blank=True, null=True)
    apple_icon_url = models.URLField(blank=True, null=True)

    # Robots / Indexing
    index = models.BooleanField(default=True)
    follow = models.BooleanField(default=True)

    # JSON-LD Schema (Structured Data)
    job_title = models.CharField(max_length=150, default="Video Editor, Graphic Designer & Frontend Developer")
    address_region = models.CharField(max_length=100, default="Kerala")
    address_country = models.CharField(max_length=10, default="IN")
    knows_about = models.TextField(
        help_text="Comma-separated list (e.g., Video Editing, Graphic Design, Next.js, Three.js)",
        default="Video Editing, Graphic Design, Frontend Development, Next.js, Three.js, GSAP"
    )
    same_as_links = models.TextField(
        help_text="One URL per line (e.g., LinkedIn, Instagram, GitHub links)",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"SEO Metadata - {self.page_name}"


class PageKeyword(models.Model):
    page_seo = models.ForeignKey(PageSEO, related_name='keywords', on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.keyword