I'm NOT participating in AoC, not really.  
And thus also not competing.  
I haven't written or read any lines of code yet. 

I'm testing which day will gemini 3 pro thinking have issues with.  
The first 4 days were completed correctly on the first try within 1-2 minutes.  
I'd expect days 5 and 6 to be more difficult and cause a failure.

I've provided a basic coding puzzle description and instructions at the root of the repository.  
There is a folder for each day, that has task.md and input.txt.  
My "prompt" is usually just "solve day X"; when it is done, just "now solve part two of day X", and that's it. 

For day 4, given that it's a symbolic 2D map, I'm impressed there were no hiccups solving it.  
And the solution script seems to only have 20 lines or so.

Day five part two was the first where "thinking" phase started getting slower - 25 seconds for one such phase.  
The problem was still solved within 2 or at most 3 minutes.  

Day six part two had a 42-second thinking phase. The puzzle was still correctly solved within 2-3 minutes.
Day seven part one required 2 minutes of thinking, part two needed 2'20". Scripts are now 80-100 lines, and have more comments.
Day eight was again faster.
Day nine: nothing out of the ordinary.
With the latest update, I now get asked for confirmation twice (when implementation plan is ready and before running the script), may need to change that.
Updating antigravity's own task file has now failed fort he 2nd time, I wonder if this is because I'm instructing to solve all puzzles within the same chat context since day 1.

Day ten: had to start a new chat/context, because the long existing one failed to produce anything twice in a row.
This has reset some of the solution conventions (solution script naming) of the first 9 days.
This time gemini produced a small sample.txt input file, that it used for testing the solution before running it on the full input.
Part two solution (attempt one) has failed! Answer too low.
Solution has imports now, and uses linear algebra.
Initial script took maybe 10-15 seconds to run.
On second attempt the script did not produce anything after several minuts of running.
Atetmpt 3 comment:
> I've realized that the current approach is not efficient enough, even with a larger limit.
> The problem is proving to be computationally expensive.
> I'm now exploring a smarter solver design that formulates constraints properly as a convex polytope.
> The goal is to minimize a linear objective function over integer variables, and I'm checking if scipy.optimize.milp is available to solve this.
> If not, I'll implement a recursive search with pruning.
Attempt 4 was successful/correct. Total time spent solving today was 35 minutes, not the usual 10...

