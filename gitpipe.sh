git init -b main
git add .
git commit -m "change_files"
# Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
git remote add origin https://github.com/fampkin/LecturesAndHomeWorks.git
git push -u origin main