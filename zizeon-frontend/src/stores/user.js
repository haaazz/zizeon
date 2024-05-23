import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore(
  "usercounter",
  () => {
    const API_URL = "http://127.0.0.1:8000/";
    const loginUser = ref({
      age: 0,
      email: "",
      first_name: "",
      gender: "Female",
      income: 0,
      job: "",
      last_name: "",
      nickname: "",
      pk: 0,
      username: "",
      token: "",
      deposits: [],
      savings: [],
    });

    const isLogin = computed(() => loginUser.value.token !== "");

    const logIn = function (payload) {
      const username = payload.username;
      const password = payload.password;
      console.log(payload);
      return axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          console.log("로그인 잘 됨 !!!!ㅎㅎ");
          console.log(res.data);
          loginUser.value.token = res.data.key;
          console.log(res.data.key);
          axios({
            method: "get",
            url: `${API_URL}/accounts/user/`,
            headers: {
              Authorization: `Token ${res.data.key}`,
            },
          })
            .then((res2) => {
              console.log("성공!", res2.data);
              loginUser.value = {
                ...res2.data,
                token: res.data.key,
              };

              getUserOpenedProducts();
            })
            .catch((err2) => {
              console.log("실패!");
              console.log(res.data.key);
              console.log(err2);
            });
        })
        .catch((err) => console.log(err));
    };

    const signUp = function (payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      const email = payload.email;
      const nickname = payload.nickname;
      const gender = payload.gender;
      const age = payload.age;
      const job = payload.job;
      const income = payload.income;

      return axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
          email,
          nickname,
          gender,
          age,
          job,
          income,
        },
      })
        .then((res) => {
          console.log("회원가입이 완료되어씁니다");
          const password = password1;
          logIn({ username, password });
        })
        .catch((err) => console.log(err));
    };

    const logout = () => {
      loginUser.value = {
        age: 0,
        email: "",
        first_name: "",
        gender: "Female",
        income: 0,
        job: "",
        last_name: "",
        nickname: "",
        pk: 0,
        username: "",
        token: "",
      };
    };

    const getUserOpenedProducts = function () {
      axios({
        method: "get",
        url: `${API_URL}/accounts/products/`,
        headers: {
          Authorization: `Token ${loginUser.value.token}`,
        },
      })
        .then((response) => {
          loginUser.value = {
            ...loginUser.value,
            savings: response.data.savings,
            deposits: response.data.deposits,
          };
        })
        .catch((error) => {
          console.log(error);
        });
    };

    return {
      API_URL,
      signUp,
      logIn,
      isLogin,
      logout,
      loginUser,
      getUserOpenedProducts,
    };
  },
  { persist: true }
);
