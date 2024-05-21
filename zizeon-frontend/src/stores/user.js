import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('usercounter', () => {
  const API_URL = 'http://70.12.102.186:8000'

  const token = ref(null)
  
  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password

    return axios({
        method:'post',
        url: `${API_URL}/accounts/login/`,
        data: {
            username, password
        }
    })
    .then(res => {
        console.log('로그인 잘 됨 !!!!ㅎㅎ')
        console.log(res.data)
        token.value = res.data.key
        console.log(token)
    })
    .catch(err => console.log(err))


  }

  const signUp = function(payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    const email = payload.email
    const nickname = payload.nickname
    const gender = payload.gender
    const age = payload.age
    const job = payload.job
    const income = payload.income

    return axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
            username, password1, password2, email, nickname, gender, age, job, income
        }
    })
    .then(res => {
        console.log('회원가입이 완료되어씁니다')
    })
    .catch(err => console.log(err))
  }

  return { API_URL, signUp, logIn, token }
}, { persist : true } )