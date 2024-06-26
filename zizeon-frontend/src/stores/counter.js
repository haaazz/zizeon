import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const currencies = ref([]);
    const API_URL = 'http://70.12.102.186:8000';

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
