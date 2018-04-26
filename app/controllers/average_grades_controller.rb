class AverageGradesController < ApplicationController
  before_action :set_average_grade, only: [:show, :edit, :update, :destroy]

  # GET /average_grades
  # GET /average_grades.json
  def index
    @average_grades = AverageGrade.all
  end

  # GET /average_grades/1
  # GET /average_grades/1.json
  def show
  end

  # GET /average_grades/new
  def new
    @average_grade = AverageGrade.new
  end

  # GET /average_grades/1/edit
  def edit
  end

  # POST /average_grades
  # POST /average_grades.json
  def create
    @average_grade = AverageGrade.new(average_grade_params)

    respond_to do |format|
      if @average_grade.save
        format.html { redirect_to @average_grade, notice: 'Average grade was successfully created.' }
        format.json { render :show, status: :created, location: @average_grade }
      else
        format.html { render :new }
        format.json { render json: @average_grade.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /average_grades/1
  # PATCH/PUT /average_grades/1.json
  def update
    respond_to do |format|
      if @average_grade.update(average_grade_params)
        format.html { redirect_to @average_grade, notice: 'Average grade was successfully updated.' }
        format.json { render :show, status: :ok, location: @average_grade }
      else
        format.html { render :edit }
        format.json { render json: @average_grade.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /average_grades/1
  # DELETE /average_grades/1.json
  def destroy
    @average_grade.destroy
    respond_to do |format|
      format.html { redirect_to average_grades_url, notice: 'Average grade was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_average_grade
      @average_grade = AverageGrade.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def average_grade_params
      params.require(:average_grade).permit(:A, :B, :C, :D, :Other)
    end
end
