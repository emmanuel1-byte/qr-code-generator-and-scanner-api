echo "Git Automation 🤖 \n"
git status
git add .

echo  "Enter your commit message"
read MESSAGE

git commit -m "$MESSAGE"
git push origin main

echo "Changes pushed to the 'main' branch"