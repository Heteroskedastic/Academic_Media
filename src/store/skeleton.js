const state = {
    drawer : true
}

const getters = {
    drawer_getters : (state) => state.drawer,

    
}
const actions = {
    ChangeDrawer({commit}, data){
        commit('ChangeDrawer_mutation', data)
    }
}

const mutations = {
    ChangeDrawer_mutation(state, data){
        state.drawer = data
    }
}

export const skelton__store = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};