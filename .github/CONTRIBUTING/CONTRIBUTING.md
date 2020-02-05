## Code of Conduct

This project and everyone participating in it is governed by the [Justice Hub Code of Conduct](https://github.com/justicehub-in/Justice-Hub/blob/master/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior to [judiciary@civicdatalab.in](mailto:judiciary@civicdatalab.in).

## If you have questions:

* You can write us at [judiciary@civicdatalab.in](mailto:judiciary@civicdatalab.in).
* Start a discussion on our [Project Taiga Board](https://taiga.civicdatalab.in/project/apoorv-justice-data-hub/issues).
* Use [this template](https://github.com/justicehub-in/Justice-Hub/blob/master/.github/ISSUE_TEMPLATE/question.md) to create a new issue in this repository.

`NOTE: Please avoid creating github issues for questions related to the usage of the platform, you can ask them on the Taiga Board or write to us instead.`

## Setting up your Dev env
Please refer to the [wiki]().  
[TBD: add wiki link when page added.]

## Workflow

* Create an issue for a feature/bug.
* Discuss the implementation on the issue itself while attaching the supporting docs there.
* Create a new branch for the issue.
* Code in the branch.
* Open a PR using [this template](https://github.com/justicehub-in/Justice-Hub/blob/master/.github/PULL_REQUEST_TEMPLATE/pull_request_template.md) with the very first commit and add a WIP prefix to the title of the PR. e.g. `WIP: Fix #1 - add base project structure with spiders.`
* When finished with the implementation, request reviews and remove the WIP prefix.
* If approved, merge the branch. If you are merging from your local CLI(instead of Github UI), make sure your merge commit message contain `Fix #1` (for our example, the issue number is 1, replace it with whatever issue number you worked on).
* Go back and check if your issue is closed or not, if not just close it with a reference to the PR which closes it and then go ahead and delete the branch.

### Branching Model

* Protect Master Branch  
  Resources:
  * [Defining the mergeability of PRs](https://help.github.com/en/articles/defining-the-mergeability-of-pull-requests)

* Branches should be created with respect to issues with the name convention as:

      <feature_name-#issue_number> e.g. scraper-#1.


## Styleguides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- When only changing documentation, include [ci skip] in the commit title
- Consider starting the commit message with an applicable emoji:

    - :art: `:art:` when improving the format/structure of the code
    - :racehorse: `:racehorse:` when improving performance
    - :non-potable_water: `:non-potable_water:` when plugging memory leaks
    - :memo: `:memo:` when writing docs
    - :bug: `:bug:` when fixing a bug
    - :fire: `:fire:` when removing code or files
    - :green_heart: `:green_heart:` when fixing the CI build
    - :white_check_mark: `:white_check_mark:` when adding tests
    - :lock: `:lock:` when dealing with security
    - :arrow_up: `:arrow_up:` when upgrading dependencies
    - :arrow_down: `:arrow_down:` when downgrading dependencies
    - :shirt: `:shirt:` when removing linter warnings

### Python Styleguide

* We really like [Google's Python Styleguide](https://google.github.io/styleguide/pyguide.html).
  * Do not miss the `pylint` specific instructions.
* We try to stick to [Pep8](https://pep8.org/) as much as possible.

### Documentation Styleguide

* Use [Markdown](https://daringfireball.net/projects/markdown/).
* [Don’t document your code. Code your documentation.](https://medium.com/@morillas/dont-document-your-code-code-your-documentation-5b940357a829)
* [How to document source code responsibly.](https://medium.com/@andrewgoldis/how-to-document-source-code-responsibly-2b2f303aa525)
* [The Hitchhiker's guide to Documentation.](https://docs.python-guide.org/writing/documentation/)
* [A beginner’s guide to writing documentation.](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)

## How to lint locally

* [Integrating pylint in your workflow.](https://github.com/CivicDataLab/hp-fiscal-data-explorer-backend/wiki/Integrate-code-linting-to-your-workflow)

`NOTE: Any PR that needs to be merged must get a score > 8 to be passed from CI pipeline.`

## Testing
[TBD: add test instructions]

## Additional Notes

### Issues and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests.

[GitHub search](https://help.github.com/articles/searching-issues/) makes it easy to use labels for finding groups of issues or pull requests you're interested in. To help you find issues and pull requests, each label is listed with search links for finding open items with that label in `justicehub-in`. We  encourage you to read about [other search filters](https://help.github.com/articles/searching-issues/) which will help you write more focused queries.

Please open an issue on `justicehub-in/Justice-Hub` if you have suggestions for new labels, and if you notice some labels are missing on some repositories, then please open an issue on that repository.

#### Type of Issue and Issue State


| Label name | `justicehub-in`‑org :mag_right: | Description |
| --- | --- | --- |
| `enhancement` | [search][search-jh-org-label-enhancement] | Feature requests. |
| `bug` | [search][search-jh-org-label-bug] | Confirmed bugs or reports that are very likely to be bugs. |
| `question` | [search][search-jh-org-label-question] | Questions more than bug reports or feature requests. |
| `feedback` | [search][search-jh-org-label-feedback] | General feedback more than bug reports or feature requests. |
| `help-wanted` | [search][search-jh-org-label-help-wanted] | The Justice Hub core team would appreciate help from the community in resolving these issues. |
| `beginner` | [search][search-jh-org-label-beginner] | Less complex issues which would be good first issues to work on for users who want to contribute to Justice Hub. |
| `more-information-needed` | [search][search-jh-org-label-more-information-needed] | More information needs to be collected about these problems or feature requests (e.g. steps to reproduce). |
| `needs-reproduction` | [search][search-jh-org-label-needs-reproduction] | Likely bugs, but haven't been reliably reproduced. |
| `blocked` | [search][search-jh-org-label-blocked] | Issues blocked on other issues. |
| `duplicate` | [search][search-jh-org-label-duplicate] | Issues which are duplicates of other issues, i.e. they have been reported before. |
| `wontfix` | [search][search-jh-org-label-wontfix] | The Justice Hub core team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |
| `invalid` | [search][search-jh-org-label-invalid] | Issues which aren't valid (e.g. user errors). |
| `wrong-repo` | [search][search-jh-org-label-wrong-repo] | Issues reported on the wrong repository (e.g. a bug related to the [Front-end](https://github.com/justicehub-in/JH-Frontend) was reported on [Backend](https://github.com/justicehub-in/JH-Backend)). |


#### Topic Categories

| Label name | `justicehub-in`‑org :mag_right: | Description |
| --- | --- | --- |
| `documentation` | [search][search-jh-org-label-documentation] | Related to any type of documentation. |
| `performance` | [search][search-jh-org-label-performance] | Related to performance. |
| `security` | [search][search-jh-org-label-security] | Related to security. |
| `ui` | [search][search-jh-org-label-ui] | Related to visual design. |
| `api` | [search][search-jh-org-label-api] | Related to JusticeHub's public APIs. |


#### Pull Request Labels

| Label name | `justicehub-in`‑org :mag_right: | Description
| --- | --- | --- |
| `wip` | [search][search-jh-org-label-wip] | Pull requests which are still being worked on, more changes will follow. |
| `needs-review` | [search][search-jh-org-label-needs-review] | Pull requests which need code review, and approval from Justice Hub core team. |
| `under-review` | [search][search-jh-org-label-under-review] | Pull requests being reviewed by the core team. |
| `requires-changes` | [search][search-jh-org-label-requires-changes] | Pull requests which need to be updated based on review comments and then reviewed again. |
| `needs-testing` | [search][search-jh-org-label-needs-testing] | Pull requests which need manual testing. |



[search-jh-org-label-enhancement]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aenhancement
[search-jh-org-label-bug]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Abug
[search-jh-org-label-question]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aquestion
[search-jh-org-label-feedback]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Afeedback
[search-jh-org-label-help-wanted]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Ahelp-wanted
[search-jh-org-label-beginner]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Abeginner
[search-jh-org-label-more-information-needed]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Amore-information-needed
[search-jh-org-label-needs-reproduction]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aneeds-reproduction
[search-jh-org-label-triage-help-needed]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Atriage-help-needed
[search-jh-org-label-windows]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Awindows
[search-jh-org-label-linux]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Alinux
[search-jh-org-label-mac]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Amac
[search-jh-org-label-documentation]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Adocumentation
[search-jh-org-label-performance]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aperformance
[search-jh-org-label-security]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Asecurity
[search-jh-org-label-ui]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aui
[search-jh-org-label-api]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aapi
[search-jh-org-label-crash]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Acrash
[search-jh-org-label-auto-indent]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aauto-indent
[search-jh-org-label-encoding]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aencoding
[search-jh-org-label-network]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Anetwork
[search-jh-org-label-uncaught-exception]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Auncaught-exception
[search-jh-org-label-git]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Agit
[search-jh-org-label-blocked]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Ablocked
[search-jh-org-label-duplicate]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aduplicate
[search-jh-org-label-wontfix]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Awontfix
[search-jh-org-label-invalid]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Ainvalid
[search-jh-org-label-package-idea]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Apackage-idea
[search-jh-org-label-wrong-repo]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Awrong-repo
[search-jh-org-label-editor-rendering]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aeditor-rendering
[search-jh-org-label-build-error]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Abuild-error
[search-jh-org-label-error-from-pathwatcher]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aerror-from-pathwatcher
[search-jh-org-label-error-from-save]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aerror-from-save
[search-jh-org-label-error-from-open]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aerror-from-open
[search-jh-org-label-installer]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Ainstaller
[search-jh-org-label-auto-updater]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aauto-updater
[search-jh-org-label-deprecation-help]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Adeprecation-help
[search-jh-org-label-electron]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Ajusticehub-in+label%3Aelectron
[search-jh-org-label-wip]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Ajusticehub-in+label%3Awip
[search-jh-org-label-needs-review]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Ajusticehub-in+label%3Aneeds-review
[search-jh-org-label-under-review]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Ajusticehub-in+label%3Aunder-review
[search-jh-org-label-requires-changes]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Ajusticehub-in+label%3Arequires-changes
[search-jh-org-label-needs-testing]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Ajusticehub-in+label%3Aneeds-testing

[beginner]:https://github.com/search?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3Abeginner+label%3Ahelp-wanted+user%3Ajusticehub-in+sort%3Acomments-desc
[help-wanted]:https://github.com/search?q=is%3Aopen+is%3Aissue+label%3Ahelp-wanted+user%3Ajusticehub-in+sort%3Acomments-desc+-label%3Abeginner


`NOTE: The contribution guidelines are inspired by awesome contribution guidelines from Atom: https://github.com/atom/atom/blob/master/CONTRIBUTING.md`
