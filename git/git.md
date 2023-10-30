# GIT

### git patch
```shell
> git diff > some.patch
# or if changes commited:
> git format-patch -1
# Then
> git apply some.patch
```

### Merge
#### Merge with sqush of some dev branch to sprint branch
```bash
git checkout sprint_81
git merge --squash bugfix
git commit
```

### GIT submodule update submodules from scratch
```bash
git submodule update --init --recursive
```

### Rebase

#### Rebase to pick necessary commits
```bash
git rebase -i origin/sprint_71
```
[GIT cherry-pick, rebase multiple commits to other branch](https://stackoverflow.com/questions/1670970/how-to-cherry-pick-multiple-commits)

```bash
git rebase --onto a b f
# if squash is required
git rebase --onto a b f -i

# Into origin/master commits from 4517bd29042706c9bf7c68a25e1cdd2c3e4bd0e3 (not included) till origin/EPMMOOC-9938_AB_FE_ACCESSIBILITY_Modify_EDX_UI_to_increase_accessibility_options
git rebase --onto origin/master 4517bd29042706c9bf7c68a25e1cdd2c3e4bd0e3 origin/EPMMOOC-9938_AB_FE_ACCESSIBILITY_Modify_EDX_UI_to_increase_accessibility_options
```

### GIT LOG
```bash
git log --graph
git log --graph --pretty=oneline --all
```

### GIT tags
```bash
git tag MOOC_3.3.13
git push --tags
```

### Remove in origin:
```bash
git push --delete origin MOOC_3.3.13
```

### Remove locally:
```bash
git tag --delete MOOC_3.3.13
```

### GIT search commits which intruduse the <search string>
```bash
git log -S <search string> --source --all
git log -S "eav_value_test_events" --source --all
git log -G "eav_value_test_events" --source --all
```

### The last commit where the file was deleted
```bash
git rev-list -n 1 HEAD -- big3_data_main_app/settings_local.tpl.py
```

### Observe commits without branches
```bash
git reflog
```
