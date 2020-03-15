# Application in Scheduling

## Scheduling: Makespan minimization
* There are *m* **machines** in a factory.
* There are *n* **jobs** to be processed.
* A job j has a give **processing time** ![](https://i.imgur.com/7sQ7Wmp.png)
    *For a machine to complete job j, it needs to spend ![](https://i.imgur.com/A0wASAA.png) amount of time.
    *j is completed at Cj if Cj = Sj + Pj, where Sj is starting time
* A typical scheduling problem is to schedule these jobs to machines to **minimize the makespan**

---

## Example
* Jobs [3, 3, 3, 3, 4, 5, 5, 6, 7, 8]
* 3 Machines
* Schedule 1 (makespan = 18):
    * [3, 3, 3, 6], [4, 4, 7], [5, 5, 8]
* Schedule 2 (makespan = 16):
    * [3, 3, 4, 6], [4, 5, 7], [5, 3, 8]

---

## Makespan minimization
* load balancing
    * fairly jobs allocation
    * save utility fees
* NP-hard problem, however
* Therefore, several heuristic algorithms(經驗法則) have been developed
    * easy to implement, excecute
    * time efficient
    * nearly optimal

---

## Longest processing time first (LPT algorithm)
* sort all jobs
* use greedy (for each iteration, makes the best choice atm)
* in fact, w/o sorting, it works well
* it has been shown to have a worst-case performance guarantee
    * Let z* be the optimal solution
    * Let zLPT be the LPT algo. solution
    * For any instance, we have zLPT/z* <= 4/3
    * the approximation factor of LPT is 4/3

---

## Inventory control
* commonly needed in practice
* retailers keep inventory of products
* manufactureres keep inventory of raw materials
* Why?
  * buffer S and D
  * balance between fixed ordering cost and variable holding cost
* How?
  * inventory policies(存貨政策)
    * when
    * how
    * from whom (if multiple suppliers)

---

## Inventory policies
* **(Q, R) policy**
  * check the amount of inventory level L on a certain basis
  * if L < R(Re-order point), order Q units; otherwise, do nothing.
* **(s, S) policy**
  * check the amount of inventory level L on a certain basis
  * if L < s(Re-order point), order *up to* Q units; otherwise, do nothing.

---

## Optimizing (Q, R) policy
* choose Q, R base on three relevant cost:
  * inventory cost
  * ordering cost
  * shortage cost: loss sales upon shortage

---

## Logistics and Transportation 物流與運輸
* common in supply chain management and service management
  * route, quantity, timing, and transportation mode selection
  * shipping goods among suppliers, manufacturers and retailers
  * shipping goods to consumers

---

## Traveling Salesman Problem (NP hard)
* sequencing problem, there are n! feasible route
* sometimes vehicle capacity is also an issue
* TSP is the special case where capacity is unlimited
* here use greedy to solve
  * at the origin, go to the next which is the closest
  * during each iteration, go to the next closest and unvisited
  * at the end, back to the origin
