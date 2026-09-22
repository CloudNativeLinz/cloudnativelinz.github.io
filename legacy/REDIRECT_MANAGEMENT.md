# Event URL Redirect Management

This guide explains how to manage redirects for your Jekyll-generated event pages to prevent broken links when titles change.

## How It Works

1. **Stable URLs**: Event pages are now generated using stable `slug` fields instead of titles
2. **Automatic Redirects**: When you change a title, add the old URL to `redirect_from` array
3. **SEO-Friendly**: Redirects use proper HTTP redirects and canonical URLs

## Configuration

The setup includes:
- **Modified `_config.yml`**: Uses `slug` field for URL generation
- **Custom Plugin**: `_plugins/datapage_redirect_generator.rb` handles redirects
- **Redirect Layout**: `_layouts/redirect.html` creates proper redirect pages

## Managing Redirects

### Step 1: Generate Slugs
Run the management script to ensure all events have stable slugs:
```bash
ruby manage_redirects.rb
```

### Step 2: Update Event Data
When changing a title, follow this pattern in `_data/events.yml`:

```yaml
- id: 34
  title: "New Updated Title"           # New title
  slug: "stable-slug-name"             # Keep this the same!
  redirect_from:                       # Add old URLs here
    - "/events/meetup/old-title-slug"
    - "/events/meetup/another-old-url"
  # ... rest of event data
```

### Step 3: Build and Deploy
```bash
bundle exec jekyll build
```

## Example Scenario

**Original Event:**
```yaml
- id: 34
  title: "Beyond k8s and OpenSource Metrics"
  slug: "beyond-k8s-and-opensource-metrics"
```
URL: `/events/meetup/beyond-k8s-and-opensource-metrics/`

**After Title Change:**
```yaml
- id: 34
  title: "Advanced Kubernetes and Metrics"  # New title
  slug: "beyond-k8s-and-opensource-metrics" # Same slug = same URL
  redirect_from:
    - "/events/meetup/34-cloud-native-computing-linz-meetup"  # Old URL still works
```

## Benefits

1. **No Broken Links**: Old URLs automatically redirect to new ones
2. **SEO Preserved**: Search engines follow redirects properly
3. **User-Friendly**: Visitors never see 404 errors
4. **Future-Proof**: Easy to add more redirects as needed

## Testing

1. Build the site: `bundle exec jekyll build`
2. Serve locally: `bundle exec jekyll serve`
3. Test old URLs in browser to confirm redirects work
4. Check that new URLs display the correct content

## Maintenance

- Keep slugs stable once created
- Always add old URLs to `redirect_from` when changing titles
- Run `ruby manage_redirects.rb` to ensure all events have slugs
- Regularly test redirects after deployments