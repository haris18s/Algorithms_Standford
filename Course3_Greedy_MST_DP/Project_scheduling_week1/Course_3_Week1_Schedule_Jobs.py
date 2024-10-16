#! usr/bin/env python3

def parse_file(file_name):
    """
    Parses the job data from a specified text file.
    Input:
        file_name (str): The name of the text file containing job data.
                          The first line contains the number of jobs,
                          followed by lines containing job weight and length.

    Output:
        Tuple[List[Tuple[int, int, int]], List[Tuple[int, int, float]]]:
            Two lists of tuples:
            a) Each tuple contains (weight, length, weight-length difference).
            b) Each tuple contains (weight, length, weight/length ratio).
    """

    jobs_diff = []
    jobs_ratio = []
    with open(file_name, 'r') as f:
        #skip the first line
        next(f)
        for line in f:
            weight, length = map(int, line.split())
            diff = weight - length
            ratio = weight /length
            jobs_diff.append((weight, length, diff))
            jobs_ratio.append((weight, length, ratio))

    return jobs_diff, jobs_ratio

def schedule_job(jobs):
    """
    Schedules jobs based on their weight-length difference and weight/length ratio.

    Input:
        jobs (List[Tuple[int, int, float]]): List of jobs with weight, length,
        and either weight-length difference or weight/length ratio.

    Output:
        List[Tuple[int, int, float]]: Sorted list of jobs based on the criteria:
        primarily by the negative difference/ratio, and secondarily by weight.
    """
    # Sort jobs first by negative difference (to sort in descending order) and then by weight
    sorted_list = sorted(jobs, key=lambda x: (-(x[2]), -x[0] ))
    return sorted_list

def computeSumWeightsCompletion(sorted_jobs):
    """
    Calculates the total weighted completion time for a sorted list of jobs.

    Input:
        sorted_jobs (List[Tuple[int, int, int]]): Sorted list of jobs with weight,
        length, and weight-length difference.

    Output:
        int: The total sum of weighted completion times for the scheduled jobs.
    """
    completion_time =0
    total_weight_comp_time = 0
    for job in sorted_jobs:
        #list of each job
        weight,length, diff = job


        # Update cumulative completion time with the current job's length
        weighted_completion_time = weight *completion_time

        # Accumulate the total weighted completion time
        total_weight_comp_time +=weighted_completion_time
    return total_weight_comp_time

def main():
    """
    Main function to execute the scheduling algorithm for jobs.
    Parses job data from a file, schedules jobs, and computes the total weighted
    completion time based on different criteria (difference and ratio).
    """
    jobs_diff, jobs_ratio = parse_file('jobs_data.txt')

    # sort the jobs list for jobs_diff and jobs ratio
    sorted_list_diff =  schedule_job(jobs_diff)
    sorted_list_ratio =  schedule_job(jobs_ratio)

    # compute total sums of wieght for diff and ratio
    totalWeightDiff = print(f"Total sum weight for Diff: {computeSumWeightsCompletion(sorted_list_diff)}")
    totalWeightRatio = print(f"Total sum weight for Ratio: {computeSumWeightsCompletion(sorted_list_ratio)}")

if __name__ == '__main__':
    main()