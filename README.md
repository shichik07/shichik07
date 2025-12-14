# Personal Website - Julius Kricheldorff

Personal [website](https://julius-kricheldorff.com/) created using [distill](https://github.com/rstudio/distill).

## Build Instructions

This website is built using R Markdown and the Distill package. To build locally:

1. Install required R packages:
   ```r
   install.packages(c("distill", "rmarkdown"))
   ```

2. Build the website:
   ```r
   rmarkdown::render_site()
   ```

3. The built site will be generated in the `docs/` directory, which is configured for GitHub Pages deployment.

## Project Structure

- `index.Rmd` - Homepage content
- `projects.Rmd` - Projects page
- `CV.rmd` - Curriculum vitae page
- `_site.yml` - Site configuration and navigation
- `theme2.css` - Active theme stylesheet
- `files/` - Static assets (CV PDF, etc.)

## Deployment

The site is configured to deploy to GitHub Pages from the `docs/` directory. Push changes to the main branch to trigger automatic deployment.
