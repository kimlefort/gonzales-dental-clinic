# Put this project on GitHub

This archive contains the latest clinic-card selection change. Extract the ZIP and open the extracted folder in VS Code. Upload the extracted source files, not the ZIP itself.

## Recommended: a private repository

The clinic has not yet approved this proposal or public reuse of its branding and photography. Keep the repository private until those permissions are confirmed. No open-source license is supplied for third-party photos or branding.

1. Create an empty private repository on GitHub. Do not initialize it with another README, license or .gitignore.
2. Open a terminal in the extracted folder containing `manage.py` and run:

   ```sh
   git init
   git add .
   git status
   ```

3. Review the staged file list. It should not contain `.venv`, `.env`, SQLite databases, ZIP archives or private files. The supplied `.gitignore` excludes these.
4. Create the first commit:

   ```sh
   git commit -m "Add Gonzales Dental website proposal"
   git branch -M main
   ```

5. Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with the repository details you created, then run:

   ```sh
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   git push -u origin main
   ```

Use your normal GitHub authentication when prompted. Do not place passwords or tokens in source files or remote URLs.

## Repository upload is not a production launch

These settings are for a local design preview: `DEBUG=True`, a placeholder Django secret, and an older Python/Django runtime. Uploading the code does not configure hosting. Before deploying, upgrade to a supported runtime, configure secrets and production settings, confirm clinic content and image permissions, and review privacy requirements. See `README.md` and `CONTENT_SOURCES.md`.

The ZIP excludes the local database. Run the README's migrations after setting up your environment to create your own empty database. No clinic appointments or credentials are included.
