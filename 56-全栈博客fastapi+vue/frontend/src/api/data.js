import axios from "./axios"


export function index_active_user(params){
    return axios.request({
        url:'/index/active_user',
        method:'get',
        params
        })}


export function index_table_data(params){
    return axios.request({
        url:'/index/table_data',
        method:'get',
        params
        })}

export function admin_index_line_chart_data(params){
    return axios.request({
        url:'/index/line_chart_data',
        method:'get',
        params
        })}

export function admin_index_pie_chart_data(params){
    return axios.request({
        url:'/index/pie_chart_data',
        method:'get',
        params
        })}

export function admin_index_histogram_data(params){
    return axios.request({
        url:'/index/histogram_data',
        method:'get',
        params
        })}
// export const index_active_user=(params) =>{
//     return axios.request({
//         url:axios.baseUrl+'/index/active_user',
//         method:'get',
//         params
//     })
//}

