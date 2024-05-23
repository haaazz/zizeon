import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useDepositStore = defineStore(
  "depositcounter",
  () => {
    const deposits = ref([]);
    const depositoptions = ref([]);
    const API_URL = "http://127.0.0.1:8000/";
    const getDeposit = function () {
      return axios({
        method: "get",
        url: `${API_URL}/products/deposit/`,
      })
        .then((res) => {
          deposits.value = res.data.deposits;
          depositoptions.value = res.data.options;
        })
        .catch((err) => console.log(err));
    };

    return { deposits, API_URL, getDeposit, depositoptions };
  },
  { persist: true }
);
