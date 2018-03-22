class StudentsController < ApplicationController

  before_action :authenticate_studen!, only: []

  def index
    redirect_to courses_url
  end

end
