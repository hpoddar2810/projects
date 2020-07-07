# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def siftDown(tree, li, i):
    print("shiftdown:")
    print("tree: ", tree)
    print("li: ", li)
    print("i: ", i)
    n = len(li) - 1
    k = i

    l = 2*i + 1
    if l <= n:
        if li[tree[l]] < li[tree[i]]:
            print("2 left: ", l)
            k = l
        elif li[tree[l]] == li[tree[i]]:
            if tree[l] < tree[i]:
                k = l
    
    r = 2*i + 2
    if r <=  n:
        if li[tree[r]] < li[tree[i]]:
            print("right: ", r)
            if k == l:
                if li[tree[l]] > li[tree[r]]:
                    k = r
                
            else:
                k = r
        elif li[tree[r]] == li[tree[i]]:
            print("sbqnjbj")
            if k == l or tree[r] < tree[i]:
                if li[tree[l]] > li[tree[r]] or tree[l] > tree[r]:
                    k = r
            

    
    if k != i:
        tree[i], tree[k] = tree[k], tree[i]
        print("tree:", tree)
        return siftDown(tree, li, k)

    else:
        return tree



def buildHeap(li):
    n = len(li) - 1
    tree = list(range(n+1))
    for i in range(n//2, -1, -1):
        print("before siftdown: ", tree)
        print(i)
        tree = siftDown(tree, li, i)
        print('After shiftdown: ', tree)

    return tree


def getMin(tree):
    return tree[0]


def changepriority(tree, li, value):
    print("9 priority changing: ", value, tree)
    return siftDown(tree, li, 0)



def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    #result = []
    # next_free_time = [0] * n_workers
    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job

    # #return result
    result = []
    end_time = jobs[:n_workers]
    print("1: end_time: ", end_time)
    tree = buildHeap(end_time)
    print("2: tree:", tree)

    for j in range(n_workers):
        result.append(AssignedJob(j, 0))

    for job in jobs[n_workers:]:
        print("6 Job:",job)
        next_worker = getMin(tree)
        print("7 next worker:",next_worker)
        result.append(AssignedJob(next_worker, end_time[next_worker]))
        end_time[next_worker] += job
        print("8 end_time:", end_time)
        tree = changepriority(tree, end_time, end_time[next_worker])
    
    return result



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
