import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useDepositStore = defineStore('depositcounter', () => {
  const deposits = ref([])
  const API_URL = 'http://70.12.102.186:8000'

  const getDeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/products/deposit/`
    })
    .then(res => {
      deposits.value = res.data
    })
    .catch(err => console.log(err))
  }

  return { deposits, API_URL, getDeposit }
}, { persist : true } )