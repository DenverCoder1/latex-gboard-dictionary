## Notes about Formatting
Gboard requires a very specific format for shortcut files to work.

![format](https://user-images.githubusercontent.com/20955511/95510460-a153ec00-09be-11eb-8400-4aca07484973.png)

Each line of the file containing a shortcut must have: the shortcut (ex. `\sum`), a single tab (` `), the symbol (ex. `∑`), and another a single tab (` `) at the end of the line.

**Note**: Some editors automatically convert tabs to spaces, you can try to avoid this by copy-pasting the tabs from a different line to ensure the spacing is correct.

## Shortcut guidelines
Shortcuts must be the same as the command from LaTeX or resemble the LaTeX shortcuts. If typing the symbol is complex in LaTeX, a shorter shortcut may be used as long as it is in the style of LaTeX commands.

It is at the discretion of the project maintainer to decide whether a certain shortcut should be accepted or not.

## Setup
* Fork the Repository.
* Clone it to the local machine. This can be done either by using `git clone https://github.com/<your_github_username>/LaTeX-Gboard-Dictionary` or directly by using github desktop.
* Open the folder on VS Code.

## Issues
* Choose an issue to work on from [Issues](https://github.com/DenverCoder1/LaTeX-Gboard-Dictionary/issues) and claim that issue.
* After the issue is assigned to you, start working on it. 

## Making changes locally
* While making new changes to this repo make sure to **create a new branch** everytime.
* Make the changes that are needed.
* Save them.
* Use `git add .` command in terminal.
* Then use `git commit -m "Enter a message that tells about the changes you made"` in terminal.

## Pull Request
* Add upstream as the main repository using `git remote add upstream https://github.com/DenverCoder1/LaTeX-Gboard-Dictionary.git` command in terminal.
* Push changes to origin i.e. your forked repository by using `git push origin master`.
* Before making pull request whether your forked repository is updated. For this use `git pull upstream master` command in the terminal.
* Make sure to test the file after making changes by making a compressed folder (zip) containing the txt file in a folder.
* Create a pull request with relevant heading. 
* Add supporting screenshots to establish the areas you have worked on.
* The repository maintainers will review your pull request and accordingly merge it or request changes.  