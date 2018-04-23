Rails.application.routes.draw do
  get 'upload/index'

  resources :yourplans
  resources :static_workloads
  resources :schedules
  resources :average_grades
  resources :tracks
  resources :professors
  resources :courses
  resources :upload
  devise_for :students

  root 'students#index'
  mount Thredded::Engine => '/forum'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
