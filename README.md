# UniQuiz DZ — Django starter

A starter university quiz platform with student signup/login, course and quiz data models, objective-question grading, teacher dashboard, result page and teacher email notification.

## 1. Requirements
- Python 3.10+
- Internet connection for Bootstrap CDN (can be replaced with local assets)

## 2. Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/

## 3. Create sample data
1. Sign in to `/admin/` with the superuser.
2. Create a normal user for the teacher and mark `Staff status`.
3. Create student users through `/signup/`.
4. Create a Course and select the teacher; add student accounts in the Students field.
5. Create a Quiz under the course, then add Questions and AnswerOptions.
6. Mark exactly one AnswerOption as correct for each single-choice question.
7. Sign in as teacher and publish the quiz from the dashboard.
8. Sign in as an enrolled student and take the quiz.

## 4. Email
By default, email is printed in the terminal (console backend). For real email, configure SMTP environment variables and replace `EMAIL_BACKEND` in `config/settings.py` with `django.core.mail.backends.smtp.EmailBackend`. Never commit real credentials.

## 5. Current MVP limitations
- Student signup is open; production needs teacher/admin approval.
- One attempt per student per quiz; no retakes yet.
- The starter supports single-choice grading; true/false can use two options.
- Duration is displayed but server-side timed submission is not implemented yet.
- No quiz authoring UI yet; create courses/questions in Django Admin.
- Teacher email notification contains a summary; detailed report is available in the teacher dashboard.
- No PDF/Excel export endpoint yet; browser print-to-PDF is available.
- Add automated tests, role permissions, audit logs, CSRF/security review, rate limits, backups and privacy controls before real student deployment.

## 6. Trilingual rollout
Django language switching is wired for English, French and Arabic. Translate visible labels using Django gettext (`{% trans %}`) and create `.po` catalogues with `django-admin makemessages -l fr -l ar`, then compile with `django-admin compilemessages`. The starter content is currently primarily English; full Arabic/French translation and RTL styling are next tasks.


## Google Stitch screens included

Your five exported Stitch HTML screens are preserved under `static/stitch/`:

- Teacher dashboard: `/static/stitch/teacher-dashboard/TeacherDashboard.html`
- Quiz builder: `/static/stitch/quiz-builder/QuizCreationInterface.html`
- Student exam: `/static/stitch/student-exam/StudentExamExperience.html`
- Analytics reports: `/static/stitch/analytics-reports/ClassAnalyticsAndRanking.html`
- Authentication/settings: `/static/stitch/auth-notifications/AuthAndNotificationSettings.html`

The relative links between the five exported pages are preserved by this folder structure. Open these URLs after starting Django to preview the designs.

**Integration status:** these are currently preserved as Stitch-generated frontend previews, not yet data-connected Django templates. Their sample statistics, names and grades are demonstration content. The next implementation step is to convert each screen into Django templates and replace sample content with database-backed views and permissions.

The design system is preserved in `STITCH_DESIGN_SYSTEM.md`.


## Deploy this Django project to Vercel

Vercel now supports Django with automatic framework detection. Keep `manage.py` and `requirements.txt` in the repository root; a custom `vercel.json` is not required for this Django setup.

### Recommended deployment steps

1. Create a GitHub repository and upload the contents of this project (not the ZIP file itself).
2. In Vercel, choose **Add New → Project**, import that GitHub repository, and deploy.
3. Before using the deployed app with real student data, create a managed PostgreSQL database (for example, from a provider supported by your account).
4. In Vercel → Project → Settings → Environment Variables, add:
   - `DJANGO_SECRET_KEY`: a long, random secret; never commit it.
   - `DATABASE_URL`: the PostgreSQL connection URL supplied by your database provider.
   - `DJANGO_DEBUG`: `False`
   - `CSRF_TRUSTED_ORIGINS`: `https://YOUR-PROJECT.vercel.app` (replace with your real Vercel domain; add custom domain origins separated by commas if needed).
   - `EMAIL_BACKEND`: `django.core.mail.backends.smtp.EmailBackend` (only when configuring real SMTP)
   - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`: values from your email provider.
5. Redeploy after adding environment variables.
6. Run database migrations against the production PostgreSQL database using a controlled deployment/management workflow before opening registration to users.

### Important production notes

- SQLite is only the local-development fallback. Vercel's function filesystem is not persistent storage for a production database.
- Do not store uploaded student files on the function filesystem; use object storage if uploads are added.
- Do not run `createsuperuser` or migrations on every web request. Run migrations once as a release/deployment task using a secure, controlled process.
- The Stitch HTML screens are previews. They are not yet connected to Django database-backed views.
- Before real university use, implement teacher approval/roles, secure quiz authoring, server-enforced exam timers, audit logging, backups, rate limiting, privacy controls and automated tests.
- Never publish secret keys, database URLs, or email passwords in GitHub.
