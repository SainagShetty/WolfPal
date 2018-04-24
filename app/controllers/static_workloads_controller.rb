class StaticWorkloadsController < ApplicationController
  before_action :set_static_workload, only: [:show, :edit, :update, :destroy]

  # GET /static_workloads
  # GET /static_workloads.json
  def index
    @static_workloads = StaticWorkload.all
  end

  # GET /static_workloads/1
  # GET /static_workloads/1.json
  def show
  end

  # GET /static_workloads/new
  def new
    @static_workload = StaticWorkload.new
  end

  # GET /static_workloads/1/edit
  def edit
  end

  # POST /static_workloads
  # POST /static_workloads.json
  def create
    @static_workload = StaticWorkload.new(static_workload_params)

    respond_to do |format|
      if @static_workload.save
        format.html { redirect_to @static_workload, notice: 'Static workload was successfully created.' }
        format.json { render :show, status: :created, location: @static_workload }
      else
        format.html { render :new }
        format.json { render json: @static_workload.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /static_workloads/1
  # PATCH/PUT /static_workloads/1.json
  def update
    respond_to do |format|
      if @static_workload.update(static_workload_params)
        format.html { redirect_to @static_workload, notice: 'Static workload was successfully updated.' }
        format.json { render :show, status: :ok, location: @static_workload }
      else
        format.html { render :edit }
        format.json { render json: @static_workload.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /static_workloads/1
  # DELETE /static_workloads/1.json
  def destroy
    @static_workload.destroy
    respond_to do |format|
      format.html { redirect_to static_workloads_url, notice: 'Static workload was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_static_workload
      @static_workload = StaticWorkload.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def static_workload_params
      params.require(:static_workload).permit(:syllabus_id, :core, :assignments, :exams, :project)
    end
end
