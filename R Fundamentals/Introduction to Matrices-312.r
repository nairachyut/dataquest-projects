## 2. Combine Vectors ##

harvard <- c(1,1,1,1,3)
stanford <- c(2,9,3,4,10)
MIT <- c(3,3,2,2,1)
cambridge <- c(4,2,6,13,48)
oxford <- c(5,7,12,9,15)
columbia <- c(6,13,13,12,4)

uni_vector <- c(harvard, stanford, MIT, cambridge, oxford, columbia)

## 3. Creating a Matrix ##

uni_vector <- c(harvard, stanford, MIT, cambridge, oxford, columbia)

uni_matrix <- matrix(uni_vector, nrow=6, ncol=5, byrow = TRUE)
print(uni_matrix)

## 4. Vector & Matrix Data Types ##

columbia_types <- c("columbia",6,13,13,12,4)
type <- class(columbia_types)
print(type)

## 5. Naming Rows And Columns ##

categories <- c("world_rank","quality_of_education","influence","broad_impact","patents")
universities <- c("Harvard","Stanford","MIT","Cambridge","Oxford","Columbia")

rownames(uni_matrix) <- universities
colnames(uni_matrix) <- categories
named_uni_matrix <- uni_matrix
print(named_uni_matrix)

## 6. Finding the dimensions of the matrix ##

tuition <- c(43280,45000,45016,49350,28450,55161)

print(dim(uni_matrix))
print(length(tuition))
equality <-  dim(uni_matrix)[1] == length(tuition)
print(equality)

## 7. Creating new columns and rows ##

tuition <- c(43280,45000,45016,49350,28450,55161)

uni_matrix <- cbind(uni_matrix, tuition)
print(uni_matrix)

## 8. Subsetting And Indexing A Matrix By Element ##

oxford_influence <- uni_matrix["Oxford","influence"]
stanford_impact <- uni_matrix["Stanford","broad_impact"]
cambridge_patents <- uni_matrix["Cambridge","patents"]
MIT_world_rank <- uni_matrix["MIT","world_rank"]

## 9. Subsetting a Matrix by Rows & Columns ##

world_rank <- uni_matrix[,"world_rank"]
columbia <- uni_matrix["Columbia",]
patents <- uni_matrix[,"patents"]

## 10. Sorting a Matrix ##

top_edu <- sort(uni_matrix[,"quality_of_education"])
low_cost <- sort(uni_matrix[,"tuition"])

## 11. Sorting Then Previewing Data ##

top_edu <- sort(uni_matrix[,"quality_of_education"])
low_cost <- sort(uni_matrix[,"tuition"])

top_two_edu <- head(top_edu, 2)
two_low_cost <- head(low_cost, 2)