# AtomGit 文档协作操作卡

官方文档核对日期：2026-10-30。下述为浏览器任务指引，未声称已在课程账号中实操。当前界面、权限和项目规则优先。

## 具体反馈

先读目标项目的贡献要求，搜索已有 Issue。确有新问题时，进入 Issue 列表的新建入口，填写能定位的标题及版本、动作、实际结果、期望结果。预览后提交；已有相关问题就补充相关新信息，不重复提交。来源：[创建 Issue](https://docs.atomgit.com/docs/help/home/org_project/issue/create_issue/)。

## 文档修改与 PR

1. 确认自己能在哪里改。共同仓库允许创建分支时，从约定基线新建一个描述目的的分支；没有写权限但允许 Fork 时，先 Fork 到自己的账户，再在副本里建立修改分支。若该项目不允许，就按规则提供反馈。
2. 确认当前选中的是修改分支，在浏览器打开目标文档，编辑并提交。方法见第十章操作卡。仅修改本次问题有关内容，保留来源与别人的工作。
3. 在 Pull Requests 新建入口选择自己的源分支和原项目约定的目标分支。核对仓库所有者与分支名称，查看实际差异，填写原因、关联问题及确实做过的检查，再创建请求。
4. 有意见时在该 PR 中回应。继续在同一源分支修订并提交，让请求包含更新；重新检查完整差异，避免无关变动混入。
5. 只有具备权限且符合项目规则时才合并；否则等待维护者处理。合并后回到目标版本复查原问题，并记录实际状态。关闭未合并与合并不是一回事。

依据：[Fork 工作流](https://docs.atomgit.com/docs/help/home/org_project/pullrequests/pr-fork/)、[创建 PR](https://docs.atomgit.com/docs/help/home/org_project/pullrequests/pr-create/)、[文件在线操作](https://docs.atomgit.com/docs/help/home/org_project/project_manage/file_operations/online_file_operations/)、[代码审查与差异](https://docs.atomgit.com/docs/help/home/org_project/pullrequests/pr-code-review/)。

## 冲突与停下的位置

出现冲突提示，先比较双方意图。普通文本冲突可按平台提供的在线编辑能力处理，保留双方必要变化，再复查；不确定时请维护者协助，不强推、不删除他人改动，也不关闭保护规则。官方帮助：[解决冲突](https://docs.atomgit.com/docs/help/home/org_project/pullrequests/pr-sovle-conflict/)。

没有真实协作者时，可在个人练习仓库体验分支和 PR。记录“个人演练”，不要把自己切换角色的评论当成同伴评价；不必向真实上游发送演练材料。
