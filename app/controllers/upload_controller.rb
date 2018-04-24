class UploadController < ApplicationController
  def index

  end

  def create
    # Logger output is visible in the terminal
    logger.debug "New article!!!"
  end
end
