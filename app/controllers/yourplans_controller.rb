class YourplansController < ApplicationController
  before_action :set_yourplan, only: [:show, :edit, :update, :destroy]

  # GET /yourplans
  # GET /yourplans.json
  def index
    @yourplans = Yourplan.where(student_id: current_student.id)
  end

  # GET /yourplans/1
  # GET /yourplans/1.json
  def show
  end

  # GET /yourplans/new
  def new
    @yourplan = Yourplan.new
  end

  # GET /yourplans/1/edit
  def edit
  end

  # POST /yourplans
  # POST /yourplans.json
  def create
    @yourplan = Yourplan.new(yourplan_params)
    respond_to do |format|
      if Yourplan.exists?(student_id: current_student.id, courses: @yourplan.courses)
        format.html { redirect_to root_path, notice: 'Course already exists in your plan.'  }
        format.json { render json: @yourplan.errors, status: :unprocessable_entity }
      elsif @yourplan.save
        format.html { redirect_to root_path, notice: 'Course was successfully added to your plan.' }
        format.json { render :show, status: :created, location: @yourplan }
      else
        format.html { redirect_to root_path }
        format.json { render json: @yourplan.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /yourplans/1
  # PATCH/PUT /yourplans/1.json
  def update
    respond_to do |format|
      if @yourplan.update(yourplan_params)
        format.html { redirect_to @yourplan, notice: 'Yourplan was successfully updated.' }
        format.json { render :show, status: :ok, location: @yourplan }
      else
        format.html { render :edit }
        format.json { render json: @yourplan.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /yourplans/1
  # DELETE /yourplans/1.json
  def destroy
    @yourplan.destroy
    respond_to do |format|
      format.html { redirect_to yourplans_url, notice: 'Yourplan was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_yourplan
      @yourplan = Yourplan.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def yourplan_params
      params.require(:yourplan).permit(:student_id, :courses, :schedule_id)
    end
end
