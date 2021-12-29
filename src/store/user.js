
import BackendAxios from "../respo"

const state = {
    Userinfo: true,
    Projects: [],
}

const getters = {
    Userinfo_getters: (state) => state.Userinfo,
    Projects_getters: (state) => state.Projects,


}
const actions = {
    GET_USER_API({ commit }) {
        return new Promise((resolve, reject) => {
            BackendAxios.get('api/user/')
                .then(data => {
                    commit('ChangeUserinfo_mutation', data.data)
                    resolve(data)
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
    GET_USER_Project({ commit }) {
        return new Promise((resolve, reject) => {
            BackendAxios.get('api/project/')
                .then(data => {
                    commit('Projects_mutation', data.data)
                    resolve(data)
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
    GET_USER_Project_ID({ commit }, param) {
        return new Promise((resolve, reject) => {
            BackendAxios.get('api/project/'+param)
                .then(data => {
                    commit('Projects_mutation', data.data)
                    resolve(data)
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
    GET_News({ commit }, query) {
        commit
        return new Promise((resolve, reject) => {
            BackendAxios.get('api/news/'+query)
                .then(data => {
                    resolve(data)
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
    GET_ProjectNews({ commit }) {
        commit
        return new Promise((resolve, reject) => {
            BackendAxios.get('api/ProjectNews/')
                .then(data => {
                    resolve(data)
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
    POST_USER_Project({ commit }, payload) {
        commit
        return new Promise((resolve, reject) => {
            BackendAxios.post('api/project/', payload)
                .then(data => {
                    resolve(data)
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
    POST_USER_ProjectNews({ commit }, payload) {
        commit
        return new Promise((resolve, reject) => {
            BackendAxios.post('api/ProjectNews/', payload)
                .then(data => {
                    resolve(data)
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
}

const mutations = {
    ChangeUserinfo_mutation(state, data) {
        state.Userinfo = data
    }
    ,
    Projects_mutation(state, data) {
        state.Projects = data
    }

}

export const user__store = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};