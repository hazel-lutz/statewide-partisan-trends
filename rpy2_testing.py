import rpy2
import rpy2.robjects as robjects

test = robjects.r('''
        # create a function `f`
        f <- function(r, verbose=FALSE) {
            if (verbose) {
                cat("I am calling f().\n")
            }
            2 * pi * r
        }
        # call the function `f` with argument value 3
        f(3)
        ''')
print(test)

results = robjects.r('''
    results <- read.csv('2020_US_County_Level_Presidential_Results.csv')
    reqd_results <- data.frame(state_name=results$state_name, 
        county_fips=results$county_fips, 
        county_name=results$county_name, 
        votes_gop=results$votes_gop, 
        votes_dem=results$votes_dem, 
        total_votes=results$total_votes)
    state_results <- subset(reqd_results, state_name=='Kentucky')
    ''')
print(results)