import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const currencies = ref([]);
<<<<<<< HEAD
    const API_URL = "http://70.12.102.186:8000";
=======
    const API_URL = 'http://70.12.102.186:8000';
>>>>>>> b2d2aa7b00a2582c49e86d3982ec49c4b264a279

    const getCurrency = function () {
      axios({
        method: "get",
        url: `${API_URL}/currencies/exchange/`,
      })
        .then((res) => {
          currencies.value = res.data;
        })
        .catch((err) => console.log(err));
    };
    return { currencies, getCurrency };
  },
  { persist: true }
);
