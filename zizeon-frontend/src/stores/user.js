import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('usercounter', () => {
  const API_URL = 'http://70.12.102.186:8000'
  const token = ref(null)
  const username = ref('')

  const isLogin = computed(() => token.value !== null)

  const logIn = function(payload) {
    const { username: user, password } = payload

    return axios.post(`${API_URL}/accounts/login/`, { username: user, password })
      .then(res => {
        console.log('로그인 성공')
        token.value = res.data.key
        username.value = user
        return res // Promise 반환
      })
      .catch(err => {
        console.error('로그인 실패:', err.response.data)
        throw err // 에러 발생 시 Promise에서 catch로 잡을 수 있도록
      })
  }

  const signUp = function(payload) {
    const { username: user, password1, password2, email, nickname, gender, age, job, income } = payload

    return axios.post(`${API_URL}/accounts/signup/`, {
      username: user, password1, password2, email, nickname, gender, age, job, income
    })
    .then(res => {
      console.log('회원가입 완료')
      return logIn({ username: user, password: password1 })
    })
    .catch(err => {
      console.error('회원가입 실패:', err.response.data)
      throw err // 에러 발생 시 Promise에서 catch로 잡을 수 있도록
    })
  }

  const logOut = () => {
    token.value = null
    username.value = ''
  }

  return { API_URL, signUp, logIn, logOut, token, isLogin, username }
}, { persist: true })
