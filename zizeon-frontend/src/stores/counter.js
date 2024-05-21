import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const currencies = ref([])
  const API_URL = 'http://192.168.35.77:8000'

  const getCurrency = function() {
      axios({
          method:'get',
          url: `${API_URL}/currencies/exchange/`
      })
      .then(res => {
          currencies.value = res.data
      })
      .catch(err => console.log(err))
  }
  return { currencies, getCurrency }
}, { persist : true } )