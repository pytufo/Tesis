import axios from "axios";

const API_URL = "http://localhost:8081/account/";

const register = (username, email, password) => {
  return axios.post(API_URL + "register", { username, email, password });
};

const login = (email, password) => {
  return axios
    .post(API_URL + "login", {
      email,
      password,
    })
    .then((response) => {
      if (response.data.email) {
        localStorage.setItem("User", JSON.stringify(response.data));
      }
      return response.data;
    });
};

const logout = () => {
  localStorage.removeItem("User");
  return axios.post(API + "signout").then((response) => {
    return response.data;
  });
};

const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem("User"));

};

const AuthService = {
    register,
    login,
    logout,
    getCurrentUser,
}

export default AuthService;