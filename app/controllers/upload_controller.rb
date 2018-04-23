class UploadController < ApplicationController
  def index

  end

  def create
    # pyscript_path = Rails.root.join('trial.py')
    # tag_var = `python #{pyscript_path}`
    # logger.debug tag_var
    # Logger output is visible in the terminal
    logger.debug "New article!!!"
  end
end
