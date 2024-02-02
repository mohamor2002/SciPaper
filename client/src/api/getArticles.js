import articles from "../constants/articles"

const getArticles=async(search,selectedOption,startDate,endDate)=>{
  console.log(search)
  console.log(selectedOption)
  console.log(startDate)
  console.log(endDate)
    return new Promise((resolve) => {
        setTimeout(() => {
          resolve(articles);
        }, 2000);
      });
    
}

export default getArticles