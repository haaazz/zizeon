import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useArticleStore = defineStore(
  "articlecounter",
  () => {
    const articles = ref([]);
<<<<<<< HEAD
    const API_URL = "'http://70.12.102.186:8000'";
=======
    const API_URL = 'http://70.12.102.186:8000'
>>>>>>> b2d2aa7b00a2582c49e86d3982ec49c4b264a279

    // 'http://70.12.102.186:8000'

    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/articles/`,
      })
        .then((res) => {
          articles.value = res.data.sort((a, b) => b.id - a.id);
        })
        .catch((err) => console.log(err));
    };
    return { articles, API_URL, getArticles };
  },
  { persist: true }
);
