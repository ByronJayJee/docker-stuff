#* @get /hello_world
hw <- function(){
  return('Hello World!!')
}

#* @get /hello_world_name
hw2 <- function(name = 'Dude'){
  str_tmp <- paste('Hello World, ',name,'!!',sep="")
  return(str_tmp)
}

