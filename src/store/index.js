import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import {skelton__store} from './skeleton'
import {user__store} from './user'

export default new Vuex.Store({
  state: {
    UserInfo: null,

  },
  getters: {
    GetUserInfo: state => {
      return state.UserInfo
    }
  },
  mutations: {
    SetUserInfo (state, data) {
      state.UserInfo = data
    }
  },
  actions: {
   
},
  modules: {
    skelton__store,
    user__store
  }
})
